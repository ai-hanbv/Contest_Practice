# RAG_STUDY
로컬 기반 모델을 사용한 RAG

목표
1. rag 를 이용하여 제공한 정보 안에서 답하는 걸 목표
2. 모르는 질문은 "모른다" 라고 출력
3. 가능하면 finetunnig 까지

사용 모델 및 환경
  - LLM : llama3.2
  - Embedding : bge-m3
  - Framework : Langchain, Gradio
  - Code : Python
  - IDE : Vscode
  - Vector DB : Undecided


1. 해결방법
- zstandard(0.23.0) 설치 시 오류 발생
- 해결법 : poetry cache clear --all pypi

