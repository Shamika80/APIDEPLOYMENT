from flask import Flask, request, jsonify
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__)

app.config['DATABASE_URI'] = os.environ.get('DATABASE_URL')

def sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

@app.route('/sum', methods=['POST'])
def sum_route():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({'error': 'Missing num1 or num2'}), 400
    result = sum(num1, num2)

    try:
        conn = psycopg2.connect(app.config['DATABASE_URI'])
        cur = conn.cursor()
        cur.execute("INSERT INTO sums (num1, num2, result) VALUES (%s, %s, %s)", (num1, num2, result))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return jsonify({'error': f'Failed to store sum in database: {e}'}), 500

    return jsonify({'result': result})

@app.route('/sum/result/<int:result_value>', methods=['GET'])
def get_sums_by_result(result_value):
    try:
        conn = psycopg2.connect(app.config['DATABASE_URI'])
        cur = conn.cursor()
        cur.execute("SELECT num1, num2 FROM sums WHERE result = %s", (result_value,))
        sums = cur.fetchall()
        cur.close()
        conn.close()
        sum_list = [{'num1': s[0], 'num2': s[1]} for s in sums]
        return jsonify(sum_list)
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve sums from database: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))