from functools import wraps
from typing import Callable, Any, Dict

class FuncRegistry:

    def __init__(self):
        self._funcs: Dict[str, Callable[..., Any]] = {}
        self._meta:  Dict[str, Dict[str, Any]] = {}

    def register(self, **named_funcs: Callable[..., Any]) -> None:

        for name, fn in named_funcs.items():
            if not callable(fn):
                raise TypeError("Needs to be callable")
            self._funcs[name] = fn
            self._meta.setdefault(name, {})
    
    def decorator(self, name: str | None = None, **meta: Any):

        def _wrap(fn: Callable[..., Any]) -> Callable[..., Any]:
            reg_name = name or fn.__name__
            self._funcs[reg_name] = fn
            self._meta[reg_name] = {**self._meta.get(reg_name, {}), **meta}

            @wraps(fn)
            def inner(*args, **kwargs):
                return fn(*args, **kwargs)
            return inner
        return _wrap
    
    def dispatch(self, name: str, *args, **kwargs) -> Any:
        try:
            fn = self._funcs[name]
        except KeyError as e:
            raise KeyError(f"No function registered under '{name}'. "
                           f"Known: {sorted(self._funcs)}") from e
        return fn(*args, **kwargs)

    def info(self, name: str) -> Dict[str, Any]:
        return dict(self._meta.get(name, {}))

    def list(self) -> list[str]:
        return sorted(self._funcs.keys())

    def __getitem__(self, name: str) -> Callable[..., Any]:
        return self._funcs[name]


registry = FuncRegistry()

# 1) Batch register using **kwargs
def add(a, b): return a + b
def sub(a, b): return a - b
registry.register(add=add, sub=sub)

# 2) Decorator registration with metadata via **kwargs
@registry.decorator(category="math", arity=2)
def mul(a, b): return a * b

@registry.decorator(name="powi", category="math", arity=2)
def power(a, b): return a ** b

# Call by name
registry.dispatch("add", 2, 3)   # 5
registry.dispatch("mul", 4, 5)   # 20
registry.dispatch("powi", 2, 8)  # 256

# Fetch the function itself
f = registry["sub"]
f(10, 6)  # 4

# Metadata
registry.info("mul")   # {'category': 'math', 'arity': 2}
registry.list()