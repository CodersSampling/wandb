"""Use wandb to track machine learning work.

Train and fine-tune models, manage models from experimentation to production.

For guides and examples, see https://docs.wandb.ai.

For scripts and interactive notebooks, see https://github.com/wandb/examples.

For reference documentation, see https://docs.wandb.com/ref/python.
"""

from __future__ import annotations

__all__ = (
    "__version__",
    "init",
    "finish",
    "setup",
    "login",
    "save",
    "sweep",
    "controller",
    "agent",
    "config",
    "log",
    "summary",
    "Api",
    "Graph",
    "Image",
    "Plotly",
    "Video",
    "Audio",
    "Table",
    "Html",
    "box3d",
    "Object3D",
    "Molecule",
    "Histogram",
    "ArtifactTTL",
    "log_artifact",
    "use_artifact",
    "log_model",
    "use_model",
    "link_model",
    "define_metric",
    "Error",
    "termsetup",
    "termlog",
    "termerror",
    "termwarn",
    "Artifact",
    "Settings",
    "teardown",
    "watch",
)

import os
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Sequence,
    Union,
)

from wandb.analytics import Sentry
from wandb.apis import InternalApi, PublicApi
from wandb.data_types import (
    Audio,
    Graph,
    Histogram,
    Html,
    Image,
    Molecule,
    Object3D,
    Plotly,
    Table,
    Video,
    box3d,
)
from wandb.errors import Error
from wandb.errors.term import termerror, termlog, termsetup, termwarn
from wandb.sdk import Artifact, Settings, wandb_config, wandb_metric, wandb_summary
from wandb.sdk.artifacts.artifact_ttl import ArtifactTTL
from wandb.sdk.interface.interface import PolicyName
from wandb.sdk.lib.paths import FilePathStr, StrPath
from wandb.sdk.wandb_run import Run
from wandb.sdk.wandb_setup import _WandbSetup
from wandb.wandb_controller import _WandbController

if TYPE_CHECKING:
    import torch  # type: ignore [import-not-found]

__version__: str = "0.18.4.dev1"

run: Run | None
config: wandb_config.Config
summary: wandb_summary.Summary
Api: PublicApi

# private attributes
_sentry: Sentry
api: InternalApi
patched: Dict[str, List[Callable]]

def setup(
    settings: Optional[Settings] = None,
) -> Optional[_WandbSetup]:
    """<sdk/wandb_setup.py::setup>"""
    ...

def teardown(exit_code: Optional[int] = None) -> None:
    """<sdk/wandb_setup.py::teardown>"""
    ...

def init(
    job_type: Optional[str] = None,
    dir: Optional[StrPath] = None,
    config: Union[Dict, str, None] = None,
    project: Optional[str] = None,
    entity: Optional[str] = None,
    reinit: Optional[bool] = None,
    tags: Optional[Sequence] = None,
    group: Optional[str] = None,
    name: Optional[str] = None,
    notes: Optional[str] = None,
    magic: Optional[Union[dict, str, bool]] = None,
    config_exclude_keys: Optional[List[str]] = None,
    config_include_keys: Optional[List[str]] = None,
    anonymous: Optional[str] = None,
    mode: Optional[str] = None,
    allow_val_change: Optional[bool] = None,
    resume: Optional[Union[bool, str]] = None,
    force: Optional[bool] = None,
    tensorboard: Optional[bool] = None,
    sync_tensorboard: Optional[bool] = None,
    monitor_gym: Optional[bool] = None,
    save_code: Optional[bool] = None,
    id: Optional[str] = None,
    fork_from: Optional[str] = None,
    resume_from: Optional[str] = None,
    settings: Union[Settings, Dict[str, Any], None] = None,
) -> Run:
    """<sdk/wandb_init.py::init>"""
    ...

def finish(exit_code: int | None = None, quiet: bool | None = None) -> None:
    """<sdk/wandb_run.py::finish>"""
    ...

def login(
    anonymous: Optional[Literal["must", "allow", "never"]] = None,
    key: Optional[str] = None,
    relogin: Optional[bool] = None,
    host: Optional[str] = None,
    force: Optional[bool] = None,
    timeout: Optional[int] = None,
    verify: bool = False,
) -> bool:
    """<sdk/wandb_login.py::login>"""
    ...

def log(
    data: dict[str, Any],
    step: int | None = None,
    commit: bool | None = None,
    sync: bool | None = None,
) -> None:
    """<sdk/wandb_run.py::Run::log>"""
    ...

def save(
    glob_str: str | os.PathLike | None = None,
    base_path: str | os.PathLike | None = None,
    policy: PolicyName = "live",
) -> bool | list[str]:
    """<sdk/wandb_run.py::Run::save>"""
    ...

def sweep(
    sweep: Union[dict, Callable],
    entity: Optional[str] = None,
    project: Optional[str] = None,
    prior_runs: Optional[List[str]] = None,
) -> str:
    """<sdk/wandb_sweep.py::sweep>"""
    ...

def controller(
    sweep_id_or_config: Optional[Union[str, Dict]] = None,
    entity: Optional[str] = None,
    project: Optional[str] = None,
) -> _WandbController:
    """<sdk/wandb_sweep.py::controller>"""
    ...

def agent(
    sweep_id: str,
    function: Optional[Callable] = None,
    entity: Optional[str] = None,
    project: Optional[str] = None,
    count: Optional[int] = None,
) -> None:
    """<wandb_agent.py::agent>"""
    ...

def define_metric(
    name: str,
    step_metric: str | wandb_metric.Metric | None = None,
    step_sync: bool | None = None,
    hidden: bool | None = None,
    summary: str | None = None,
    goal: str | None = None,
    overwrite: bool | None = None,
) -> wandb_metric.Metric:
    """<sdk/wandb_run.py::Run::define_metric>"""
    ...

def log_artifact(
    artifact_or_path: Artifact | StrPath,
    name: str | None = None,
    type: str | None = None,
    aliases: list[str] | None = None,
    tags: list[str] | None = None,
) -> Artifact:
    """<sdk/wandb_run.py::Run::log_artifact>"""
    ...

def use_artifact(
    artifact_or_name: str | Artifact,
    type: str | None = None,
    aliases: list[str] | None = None,
    use_as: str | None = None,
) -> Artifact:
    """<sdk/wandb_run.py::Run::use_artifact>"""
    ...

def log_model(
    path: StrPath,
    name: str | None = None,
    aliases: list[str] | None = None,
) -> None:
    """<sdk/wandb_run.py::Run::log_model>"""
    ...

def use_model(name: str) -> FilePathStr:
    """<sdk/wandb_run.py::Run::use_model>"""
    ...

def link_model(
    path: StrPath,
    registered_model_name: str,
    name: str | None = None,
    aliases: list[str] | None = None,
) -> None:
    """<sdk/wandb_run.py::Run::link_model>"""
    ...

def watch(
    models: torch.nn.Module | Sequence[torch.nn.Module],
    criterion: torch.F | None = None,
    log: Literal["gradients", "parameters", "all"] | None = "gradients",
    log_freq: int = 1000,
    idx: int | None = None,
    log_graph: bool = False,
) -> Graph:
    """<sdk/wandb_watch.py::watch>"""
    ...
