
from flask import Flask, render_template, request
from base_code import chatbot_response_generator, generate_tour_plan_and_suggestions

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    response_type = None
    generated_response = None

    if request.method == 'POST':
        if 'chat_query' in request.form:
            user_query = request.form.get('chat_query', '').strip()
            if user_query:
                generated_response = chatbot_response_generator(user_query)
                response_type = 'Chat'
            else:
                generated_response = "من فضلك اكتب سؤالك."

        elif 'location' in request.form:
            location = request.form.get('location', '').strip()
            interests = request.form.get('interests', '').strip()
            try:
                duration_days = int(request.form.get('duration_days', 1))
            except ValueError:
                duration_days = 1

            if location:
                generated_response = generate_tour_plan_and_suggestions(
                    location, duration_days, interests
                )
                response_type = 'Plan'

    return render_template('index.html'
                           , result=generated_response
                           , result_type=response_type
                           )

if __name__ == '__main__':
    app.run(debug=True)