from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Titulares

class TitularesTest(APITestCase):

    def setUp(self):
        #creating superuser
        self.user = User.objects.create_superuser(username='guido', email=None, password='guido')
        self.user.save()
        #log in
        self.client.login(username='guido',password='guido')
        #creating titular fisico
        data = {"nombre":"guido","apellido":"valada","dni":"41907849","cuit":"20-123455-3"}
        self.client.post("/titulares-fisicos/", data, format="json")
        #creating titular juridico
        data = {"razon_social":"guido srl","año_fundacion":"2020","cuit":"23-123455-0"}
        self.client.post("/titulares-juridicos/", data, format="json")


    def test_get_titularesfisicos_list(self):
        response = self.client.get("/titulares-fisicos/",format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_titularesjuridicoslist(self):
        response = self.client.get("/titulares-juridicos/",format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_get_titulares_list(self):
        response = self.client.get("/titulares/",format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_titularfisico(self):
        data = {"nombre":"guido","apellido":"valada","dni":"41907849","cuit":"20-98526-3"}
        response = self.client.post("/titulares-fisicos/", data, format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


    def test_create_titularjuridico(self):
        data = {"razon_social":"guido srl","año_fundacion":"2020","cuit":"23-123455-3"}
        response = self.client.post("/titulares-juridicos/", data, format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


    def test_create_titular(self):
        data = {"tipo_titular":"fisico","nombre":"guido","apellido":"valada","dni":"41907849","cuit":"202-123455-3"}
        response = self.client.post("/titulares/", data, format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


    def test_get_titularfisico(self):
        response = self.client.get("/titulares-fisicos/1/", format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_get_titularjuridico(self):
        response = self.client.get("/titulares-juridicos/2/", format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_get_titular(self):
        response = self.client.get("/titulares/1/", format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_update_titularfisico(self):
        data = {"nombre":"guido","apellido":"valada","dni":"41907849","cuit":"20-98526-3"}
        response = self.client.put("/titulares-fisicos/1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_titularjuridico(self):
        data = {"razon_social":"guido srl","año_fundacion":"2020","cuit":"23-123455-3"}
        response = self.client.put("/titulares-juridicos/2/", data, format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_update_titular(self):
        data = {"tipo_titular":"fisico","nombre":"guido","apellido":"valada","dni":"41907849","cuit":"20-98526-3"}
        response = self.client.put("/titulares/1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_titularfisico(self):
        response = self.client.delete("/titulares-fisicos/1/", format="json")
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)


    def test_delete_titularjuridico(self):
        response = self.client.delete("/titulares-juridicos/2/", format="json")
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)


    def test_delete_titular(self):
        response = self.client.delete("/titulares/1/", format="json")
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)


    


     