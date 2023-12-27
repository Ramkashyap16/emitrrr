from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    data = request.json
    correct_answer = "correct_answer"  # Replace with actual logic
    if data['answer'] == correct_answer:
        return jsonify({'correct': True, 'feedback': 'Correct answer!'})
    else:
        return jsonify({'correct': False, 'feedback': 'Incorrect answer. Try again!'})

if __name__ == '__main__':
    app.run(debug=True)
