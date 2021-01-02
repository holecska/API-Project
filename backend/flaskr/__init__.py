import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

def paginate_questions(page, selection, req_item):
    start = (page - 1) * req_item
    end = start + req_item

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

# ----------------------------------------------------------------------------
# CORS Headers
# ----------------------------------------------------------------------------
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

# ----------------------------------------------------------------------------
# GET all Categories
# ----------------------------------------------------------------------------
    @app.route('/categories')
    def retrieve_categories():
        selection = Category.query.order_by(Category.id).all()
        categories = [category.format() for category in selection]

        return jsonify({
            'success': True,
            'categories': categories
        })

# ----------------------------------------------------------------------------
# GET all Questions / Categories
# ----------------------------------------------------------------------------
    @app.route('/questions')
    def retrieve_questions():

        selection = Question.query.order_by(Question.id).all()
        page = request.args.get('page', 1, type=int)
        current_questions = paginate_questions(page, selection, 10)

        sel_cat = Category.query.order_by(Category.id).all()
        categories = [category.format() for category in sel_cat]

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'categories': categories,
            'current_category': None
        })

# ----------------------------------------------------------------------------
# DELETE a Question by ID
# ----------------------------------------------------------------------------
    @app.route('/questions/delete/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()

            if question is None:
                abort(422)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            page = request.args.get('page', 1, type=int)
            current_questions = paginate_questions(page, selection, 10)

            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': current_questions,
                'total_questions': len(Question.query.all()),
                'current_category': None
            })
        except:
            abort(422)

# ----------------------------------------------------------------------------
# CREATE a question
# ----------------------------------------------------------------------------
    @app.route('/questions', methods=['POST'])
    def create_new_question():
        body = request.get_json()

        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        new_question = body.get('question', None)
        search = body.get('searchTerm', None)

        if body is None:
            abort(400)
        try:
            if search:
                selection = Question.query.order_by(Question.id).filter(
                    Question.question.ilike('%{}%'.format(search)))
                current_questions = paginate_questions(1, selection, 10)

                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(current_questions),
                    'current_category': None
                })
            else:
                new_category_id = int(new_category) + 1

                question = Question(answer=new_answer,
                                    category=new_category_id,
                                    difficulty=new_difficulty,
                                    question=new_question)
                question.insert()

                selection = Question.query.order_by(Question.id).all()
                page = request.args.get('page', 1, type=int)
                current_questions = paginate_questions(page, selection, 10)

                return jsonify({
                    'success': True,
                    'created': question.id
                })
        except:
            abort(422)

# ----------------------------------------------------------------------------
# GET questions by category
# ----------------------------------------------------------------------------
    @app.route('/categories/<int:category_id>/questions')
    def get_questions_by_category(category_id):
        items_per_page = 5
        selection = Question.query.order_by(Question.id).filter(
            Question.category == (category_id + 1)).all()
        page = request.args.get('page', 1, type=int)
        current_questions = paginate_questions(page, selection, items_per_page)
        total_questions = Question.query.order_by(Question.id).filter(
            Question.category == (category_id + 1)).all()

        # No Question found
        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(total_questions)
        })

# ----------------------------------------------------------------------------
# GET questions for the quizzes
# ----------------------------------------------------------------------------
    @ app.route('/quizzes', methods=['GET', 'POST'])
    def quizzes():
        body = request.get_json()

        category = body['quiz_category']
        category_id = int(category)

        previous_questions = body['previous_questions']

        if category == -1:
            questions = Question.query.order_by(Question.id).all()
        else:
            questions = Question.query.order_by(Question.id).filter(
                Question.category == (category_id + 1)).all()

        questions_ids = [question.id for question in questions]

        next_question_ids = []
        for q_id in questions_ids:
            exist = False
            for prev_question in previous_questions:
                if q_id == prev_question:
                    exist = True
            if not exist:
                next_question_ids.append(q_id)

        if (len(next_question_ids)) >= 1:
            length_possible_questions = len(next_question_ids) - 1
            random_num = random.randint(0, length_possible_questions)
            next_question_id = next_question_ids[random_num]

            next_question = Question.query.filter(
                Question.id == next_question_id).one_or_none()
            next_question_form = next_question.format()

            return jsonify({
                'success': True,
                'question': next_question_form
            })
        else:
            return jsonify({
                'success': True,
                'question': None
            })

# ----------------------------------------------------------------------------
# Error Handlers
# ----------------------------------------------------------------------------
    @ app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @ app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @ app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @ app.errorhandler(405)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405
    return app
