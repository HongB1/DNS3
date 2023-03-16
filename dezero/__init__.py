# ===================================================================
is_simple_core = False  # True
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

else:
    # from dezero.core import test_mode
    # from dezero.core import Parameter
    from dezero.core import (
        Config,
        Function,
        Variable,
        as_array,
        as_variable,
        no_grad,
        setup_variable,
        using_config,
    )
    import dezero.utils
setup_variable()
