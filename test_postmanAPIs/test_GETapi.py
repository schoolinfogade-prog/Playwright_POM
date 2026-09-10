
import pytest


#@pytest.mark.api
def test_ui(playwright):
    context=playwright.request.new_context(http_credentials={"username":"aaaa","pwd":"aaaa"})
    context=playwright.request_new_context()
    response=context.get("https://dummyjson.com/products/?limit=5", headers={"Authorization":"Bearer 12345"})
    print("hello")
    print(response.json())
    assert response.status == 200
    responsebody=response.json()
    print(responsebody["products"][0]["title"])

@pytest.mark.api
def test_post(playwright):
    context=playwright.request.new_context()
    reqbody={
                   "title":"hhh",
                   
    }
    response=context.post("https://dummyjson.com/products/add", data=reqbody)
    assert response.status==201
    print(response.json())

    
        