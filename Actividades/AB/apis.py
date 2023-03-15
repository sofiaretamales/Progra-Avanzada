from typing import Tuple, List
import requests
import json

from parametros import GITHUB_BASE_URL, GITHUB_REPO_OWNER, GITHUB_REPO_NAME
from parametros import GITHUB_USERNAME
from parametros import ANIME_BASE_URL, ANIME_NUMERO
from utils.anime import Anime

from os.path import join

def get_animes() -> Tuple[int, List[Anime]]:
    # ToDo: Completar
    respuesta = requests.get(ANIME_BASE_URL.format(ANIME_NUMERO))
    status_code = respuesta.status_code
    animes = []
    animes.append(respuesta.json())

    return status_code, animes


def post_issue(token, animes: List[Anime]) -> Tuple[int, int]:
    # ToDo: Completar
    data = {
    'title':GITHUB_USERNAME,
    'body': ', '.join(animes),
    }
    issue = requests.post(GITHUB_BASE_URL.format(join(GITHUB_REPO_OWNER, token)), data=data)
    issues = requests.get(GITHUB_BASE_URL.format(join(GITHUB_REPO_OWNER, token)))
    status_code = issue.status_code
    issue_number = len(issues)

    return status_code, issue_number


def put_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404

    return status_code


def delete_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404

    return status_code
