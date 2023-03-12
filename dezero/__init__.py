# ===================================================================
is_simple_core = True  # True
# ===================================================================

if is_simple_core:
    from dezero.core_simple import (
        Function,
        Variable,
        as_array,
        as_variable,
        no_grad,
        setup_variable,
        using_config,
    )

# else:
#     from dezero.core import Variable
#     # from dezero.core import Parameter
#     from dezero.core import Function
#     from dezero.core import using_config
#     from dezero.core import no_grad
#     # from dezero.core import test_mode
#     from dezero.core import as_array
#     from dezero.core import as_variable
#     from dezero.core import setup_variable
#     from dezero.core import Config

setup_variable()
