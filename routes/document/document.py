from flask import Blueprint, send_file
from decorators import login_required
from service import document_service


document_router = Blueprint('document', __name__)


@document_router.get('/document/generate/<schedule_id>')
@login_required
def generate_schedule(user, schedule_id):
    file_stream, document_name = document_service.generate_schedule(schedule_id)
    return send_file(file_stream, as_attachment=True, download_name=document_name)
