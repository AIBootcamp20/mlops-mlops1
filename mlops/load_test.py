import io
import os

import boto3
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def get_latest_refined_data():
    # S3에서 가장 최근 정제된 데이터를 읽어와서 DataFrame으로 반환
    bucket_name = os.getenv("S3_BUCKET_NAME")
    s3 = boto3.client('s3')

    # S3에서 preprocess/ 폴더 내의 파일 목록 가져오기
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix='preprocess/')

    if 'Contents' not in response:
        print("S3에 정제된 데이터가 없습니다.")
        return None

    # 가장 최근 파일 찾기 (마지막 파일이 최신)
    files = sorted(response['Contents'], key=lambda x: x['Key'])
    latest_file = files[-1]['Key']
    print(f"S3에서 최신 데이터를 가져오는 중: {latest_file}")

    # 파일 읽기
    obj = s3.get_object(Bucket=bucket_name, Key=latest_file)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))

    return df

if __name__ == "__main__":
    # S3 데이터 로드 테스트
    data = get_latest_refined_data()
    if data is not None:
        print("데이터 로드 완료!")
        print(data.head())
