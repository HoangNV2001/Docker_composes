from dockerspawner import DockerSpawner
from nativeauthenticator import NativeAuthenticator
# from firstuseauthenticator import FirstUseAuthenticator
import os

c.JupyterHub.authenticator_class = NativeAuthenticator
c.NativeAuthenticator.create_system_users = True
# c.JupyterHub.authenticator_class = FirstUseAuthenticator

# c.GenericOAuthenticator.enable_auth_state = True
c.Spawner.http_timeout = 300
c.JupyterHub.log_level = 'DEBUG'
c.JupyterHub.hub_ip = '0.0.0.0'

c.DockerSpawner.network_name = 'jupyterhub2'

c.DockerSpawner.remove = True

c.JupyterHub.spawner_class = DockerSpawner

c.DockerSpawner.environment = {
  'GRANT_SUDO': '1',
  'UID': '0', # workaround https://github.com/jupyter/docker-stacks/pull/420
}

c.DockerSpawner.extra_create_kwargs = {'user': 'root'}
# c.DockerSpawner.extra_create_kwargs.update({'runtime': 'nvidia'})
c.DockerSpawner.extra_host_config = {
    'network_mode': 'jupyterhub2',
    'runtime': 'nvidia',
    'shm_size' : '16G',
}
notebook_dir = '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir

c.DockerSpawner.volumes = { 'jupyterhub2-user-{username}': notebook_dir, "/data":"/data" }
c.DockerSpawner.image = "nvcr.io/nvidia/nemo:24.03.01.framework" #"cschranz/gpu-jupyter:v1.6_cuda-12.0_ubuntu-22.04" # "jupyter/datascience-notebook:latest"

# Persistence
c.JupyterHub.db_url = "sqlite:///data/jupyterhub.sqlite"

# # # Enable user registration
c.OAuthenticator.allow_all = True
c.OAuthenticator.allow_existing_users = True
c.Authenticator.allowed_users = ['admin', 'hoangnv', 'hoangvm','tungnt','tungks','tungpth','hanhlth','kiennd','minhnh','phuonguk','tuannq','phundh', 'sinhnq'] #set()
c.Authenticator.admin_users = {'admin'}
c.NativeAuthenticator.open_signup = True