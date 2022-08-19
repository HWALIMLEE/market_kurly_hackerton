from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title='서비스 API',
    description='Template-Bag, GraphDB'
)


@app.post("/create/template-bag", tags=["템플릿 장바구니"])
async def Create_My_Template_Bag():
    """
    request body 에시
    {
        "item": "2154",
        "count": 3
    }
    """
    id = '' # 내가 생성한 템플릿 장바구니의 고유 id
    return {"id": id}


@app.post("/find/template-bag", tags=["템플릿 장바구니"])
async def Find_Template_Bag_I_Want():
    """
    request body 예시
    {
        "age": "23"
        "purpose": "캠핑",
        "cost": "50000"
    }
    """
    id = '' # 이 아이디는 /get/co-bags/{id} 이 API에서 id로 사용합니다.
    return {"id": id}


@app.get("/get/template-bag/{id}", tags=["템플릿 장바구니"])
async def Get_Template_Bag_I_Want():
    return {"message": "Hello FIN"}


@app.post("/create/relation", tags=["GraphDB"])
async def Create_Node_And_Relation_In_GraphDB():
    """
    request query 예시
    {
        "match": "Product"
        "node": "Name",
        "relation": "Include"
    }
    - neo4j 쿼리 문법(Cypher)을 활용하여 해당 body를 파싱하여 GraphDB에 relation을 포함한 데이터를 넣는다.
    """
    return {"message": "Hello FIN"}


@app.get("/get/relation", tags=["GraphDB"])
async def Get_Linked_Relations():
    """
    request query 예시
    {
        "match": "베이컨",
        "node": "RELATED_FOOD",
        "hop_max_count": 2
    }
    - neo4j의 쿼리 문법(Cypher)을 활용하여 해당 body를 파싱하여 최대 얼마까지 연결되어 있는 음식을 보여줄 것인지 판단
    - 예를 들어, 왼쪽에 적어놓은 body 로 neo4j에서 쿼리하면 베이컨과 관련된 요리중에 두번째 노드까지만 찾음
    - hop_max_count가 2일때, 베이컨과 관련되어 있는 “갈릭베이컨마요 김밥” 이 뜨고 그 “갈릭베이컨 마요”와 연관되어 있는 “베이컨 김치볶음밥” 이 뜰것으로 생각됩니다.
    - GraphQL의 쿼리문을 이용하여 GraphDB에서 가져옵니다.

    type Product {
        id: ID!
        name: String!
        relatedProduct: [Food!]! @relationship(type: "RELATED_FOOD-food", direction: OUT, queryDirection: DEFAULT_DIRECTED)
    }
    """
    return {"message": "Hello FIN"}



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(8080))