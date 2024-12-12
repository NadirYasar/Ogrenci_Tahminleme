from src.OgrenciTahminleme import logger
from src.OgrenciTahminleme.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'data_ingestion'

if __name__ == '__main__':
    try:
        # Aşamanın başladığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()  # Pipeline nesnesini oluştur
        obj.main()  # Ana fonksiyonu çalıştır
        # Aşamanın tamamlandığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)  # Hata durumunda kaydet
        raise e  # Hata fırlat