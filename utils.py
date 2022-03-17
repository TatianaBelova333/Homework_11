import json


def load_candidates_from_json(file_name):
    """
    Returns list of dicts with employees' information
    (skills split by ', ' for further convenience)
    :param file_name: json
    :return: list of dicts
    """

    with open(file_name, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    for candidate in candidates:
        candidate['skills'] = candidate['skills'].split(', ')
    return candidates


def search_candidate_by_id(candidate_id, candidates):
    """
    Returns dict with candidate's info with specified id or None if id not found
    :param candidate_id:
    :param candidates:
    :return: None or dict
    """
    for candidate in candidates:
        if candidate.get('id') == candidate_id:
            return candidate


def search_candidate_by_name(name, candidates):
    candidates_by_name_search = []
    for candidate in candidates:
        candidate_name = candidate.get('name', 'неизвестно').lower().split()
        if name.lower() in candidate_name:
            candidate_found = {}
            candidate_found['id'] = candidate.get('id')
            candidate_found['name'] = candidate.get('name')
            candidates_by_name_search.append(candidate_found)
    return candidates_by_name_search



def search_candidate_by_skill(skill, candidates):
    candidates_by_skill_search = []
    for candidate in candidates:
        skills = [skill.lower() for skill in candidate['skills']]
        if skill.lower() in skills:
            candidate_found = {}
            candidate_found['id'] = candidate.get('id')
            candidate_found['name'] = candidate.get('name')
            candidates_by_skill_search.append(candidate_found)
    return candidates_by_skill_search
