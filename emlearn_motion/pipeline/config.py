
from typing import Optional
from enum import StrEnum

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError


class ExtractorType(StrEnum):
    Program = 'program'
    

class PreprocessingConfig(BaseModel):
    window_length: int = 128
    hop_length: int = 64
    extractor: ExtractorType = 'program'
    #config: ConfigDict
    columns: list[str]
    program: str = '' # XXX: should be inside a subconfig?

class DatasetConfig(BaseModel):
    name: str = ''
    groups : list[str] = []
    data_columns: list[str] = []
    classes : list[str] = []
    label_column : str = ''
    time_column : str = 'time'
    sensitivity : float = 4.0
    samplerate: int = 50

class Config(BaseModel):

    preprocessing: PreprocessingConfig
    dataset: DatasetConfig



def load_config(file_path) -> Config:

    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    try:
        model = Config(**data)
    except ValidationError as e:
        print(f"Validation error in config.yaml:")
        for error in e.errors():
            field = '.'.join(str(x) for x in error['loc'])
            print(f"  - {field}: {error['msg']}")

        raise e

    return model
