# coding: utf-8

"""
    Namely API

    Move your app forward with the Namely API Move your app forward with the Namely API

    Generated by: https://konfigthis.com
"""

from namely_python_sdk.paths.folders_id.delete import DeleteFolderByIdRaw
from namely_python_sdk.paths.folders_id_resources.delete import DeleteResourceByIdRaw
from namely_python_sdk.paths.folders.get import FoldersRaw
from namely_python_sdk.paths.folders.post import Folders0Raw
from namely_python_sdk.paths.resources_id.get import GetByIdRaw
from namely_python_sdk.paths.folders_id_resources.get import GetFolderResourcesRaw
from namely_python_sdk.paths.resources.get import ResourcesRaw
from namely_python_sdk.paths.folders_id.put import UpdateFolderNameRaw


class CompanyResourcesApiRaw(
    DeleteFolderByIdRaw,
    DeleteResourceByIdRaw,
    FoldersRaw,
    Folders0Raw,
    GetByIdRaw,
    GetFolderResourcesRaw,
    ResourcesRaw,
    UpdateFolderNameRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
