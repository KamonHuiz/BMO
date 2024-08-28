from haystack.document_stores import FAISSDocumentStore
from haystack.nodes.retriever.multimodal import MultiModalRetriever
from haystack import Pipeline

# Load the FAISS document store
document_store = FAISSDocumentStore.load(
    index_path="D:\\VSCODE\\AIC_Model\\DATABASE\\DB1_12\\my_index.faiss", 
    config_path="D:\\VSCODE\\AIC_Model\\DATABASE\\DB1_12\\my_config.json"
)

def retrieve():
    global retriever_text_to_image
    retriever_text_to_image = MultiModalRetriever(
        document_store=document_store,
        query_embedding_model="sentence-transformers/clip-ViT-L-14",
        query_type="text",
        document_embedding_models={"image": "sentence-transformers/clip-ViT-L-14"}
    )

def pipeline_setup():
    global retriever_text_to_image

    pipeline = Pipeline()
    pipeline.add_node(component=retriever_text_to_image, name="retriever_text_to_image", inputs=["Query"])

    return pipeline

def get_result(query):
    pipeline = pipeline_setup()
    
    # Retrieve results based on the query
    results = pipeline.run(query=query, params={"retriever_text_to_image": {"top_k": 200}})

    # Sort the results based on the scores
    results = sorted(results["documents"], key=lambda d: d.score, reverse=True)
    return results

def doc_to_img_dir(results):
    img_dir_list = []
    for doc in results:
        folder_file_name = doc.content.split("/")[3:]

        img_dir = "D:/MyDrive/Real_data"  # Change backslashes to forward slashes

        for item in folder_file_name:
            img_dir += "/" + str(item)  # Use forward slashes

        img_dir_list.append(img_dir)
 
    return img_dir_list


# Initialize the retriever
retrieve()
