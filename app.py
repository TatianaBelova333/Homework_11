import utils
from flask import Flask, render_template

all_candidates = utils.load_candidates_from_json('candidates.json')

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template("list.html", candidates=all_candidates)


@app.route('/candidate/<int:candidate_id>')
def candidate_page(candidate_id):
    candidate_info = utils.search_candidate_by_id(candidate_id, all_candidates)
    return render_template('card.html', candidate=candidate_info)


@app.route('/search/<candidate_name>')
def candidate_by_name(candidate_name):
    candidates_found = utils.search_candidate_by_name(candidate_name, all_candidates)
    number_of_candidates = len(candidates_found)
    return render_template('search.html', candidates=candidates_found, number_of_candidates=number_of_candidates)


@app.route('/skill/<skill>')
def candidate_by_skill(skill):
    candidates_found = utils.search_candidate_by_skill(skill, all_candidates)
    number_of_candidates = len(candidates_found)
    return render_template("skill.html", candidates=candidates_found, number_of_candidates=number_of_candidates,
                           skill=skill)


app.run()
