from flask import Blueprint
from Controllers.deleteOwnerController import delete_owner

delete_owner_bp = Blueprint('delete_owner', __name__)

@delete_owner_bp.route('/owner/<owner_id>', methods=['DELETE'])
def delete(owner_id):
    return delete_owner(owner_id)
