import pandas as pd
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

def process_batch():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    
    all_data = []

    if not RAW_DIR.exists():
        print(f"Erro: O diretório {RAW_DIR} não foi encontrado.")
        return

    print("Iniciando o processamento em lote...")


    for day_dir in RAW_DIR.iterdir():
        if day_dir.is_dir():
            dia = day_dir.name
            

            for round_dir in day_dir.iterdir():
                if round_dir.is_dir():
                    rodada = round_dir.name
                    
                    for file_path in round_dir.glob('*.txt'):
                        amostra = file_path.stem  
                        
                        try:
                            df = pd.read_csv(file_path, sep='\t')
                            
                            df['Dia'] = dia
                            df['Rodada'] = rodada
                            df['Amostra'] = amostra
                            
                            df['Datetime'] = pd.to_datetime(df['Timestamp'], unit='s')
                            
                            all_data.append(df)
                            print(f"Processado -> Dia: {dia} | Rodada: {rodada} | Amostra: {amostra}")
                            
                        except Exception as e:
                            print(f"Erro ao processar o arquivo {file_path}: {e}")

    
    if all_data:
        print("\nConcatenando todos os arquivos...")
        df_final = pd.concat(all_data, ignore_index=True)
        
        output_file = PROCESSED_DIR / 'dados_consolidados.parquet'
        
        df_final.to_parquet(output_file, index=False)
        
        print(f"\nSucesso! {len(df_final)} linhas consolidadas e salvas em: {output_file}")
    else:
        print("\nNenhum arquivo .txt encontrado para processamento.")

if __name__ == "__main__":
    process_batch()