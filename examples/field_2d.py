from dff.simulation import Simulator
from dff.visualization import default_snapshot_plot

try:
    from dfpy import (
        connect,
        GaussInput,
        Field,
        Dimension,
        SumWeightPattern,
        GaussWeightPattern,
        Sigmoid,
    )
except Exception as e:
    raise ImportError(
        "Missing dfpy (DynamicFieldPy). Install it with:\n"
        (
            "  pip install git+https://github.com/danielsabinasz/"
            "DynamicFieldPy.git"
        )
    ) from e

gauss = GaussInput(
    dimensions=[Dimension(-25, 25, 51), Dimension(-25, 25, 51)],
    mean=[8.0, 5.0],
    height=8.0,
    sigmas=[3.0, 3.0]
)

field = Field(
    dimensions=[Dimension(-25, 25, 51), Dimension(-25, 25, 51)],
    resting_level=-5.0,
    interaction_kernel=SumWeightPattern([
        GaussWeightPattern(height=0.4, sigmas=(2.0, 2.0)),
        GaussWeightPattern(height=-0.11, sigmas=(4.0, 4.0))
    ], field_size=(51, 51)),
    global_inhibition=-0.0
)


def main(no_show: bool = False) -> None:
    connect(
        gauss,
        field,
        pointwise_weights=6.0,
        activation_function=Sigmoid(1)
    )

    sim = Simulator()
    sim.simulate_until(2000)

    plot = default_snapshot_plot(field)
    plot.draw(sim.get_value(field).numpy())

    # save first so we have an image even in headless environments
    plot.figure.savefig('field_2d.png', dpi=150)
    print('Saved plot to field_2d.png')

    # show blocks when a GUI is available; returns after window is closed
    if not no_show:
        plot.figure.show()
        print('Plot window closed')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Run the 2D field example'
    )
    parser.add_argument(
        '--no-show',
        action='store_true',
        help='Do not open a GUI window (save only)'
    )
    args = parser.parse_args()

    main(no_show=args.no_show)
