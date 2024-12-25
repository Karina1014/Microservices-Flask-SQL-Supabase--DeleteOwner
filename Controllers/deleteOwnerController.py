from Services.supabase_client import get_supabase_client

def delete_owner(owner_id):

        # Ejecutar la eliminación del propietario con el id_card
        response = get_supabase_client().table('owner').delete().eq('id_card', owner_id).execute()

        # Verificar si la respuesta contiene datos (lo que indica que la eliminación fue exitosa)
        if response.data and len(response.data) > 0:
            return {"message": f"Owner with id_card {owner_id} successfully deleted."}, 200
        else:
            return {"error": f"No owner found with id_card {owner_id}."}, 404

 