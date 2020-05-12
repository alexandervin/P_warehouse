from unittest import TestCase


class SquareEquationSolverTestCase(TestCase):

    def test_solver_module_exist(self):
        try:
            import solver
        except ModuleNotFoundError:
            self.fail('Module solver non found')

    def test_solver_function_exist(self):
        import solver
        self.assertTrue(
            hasattr(solver, 'squere_equition_solver')
        )

    def test_function_accepts_args(self):
        from solver import squere_equition_solver
        try:
            squere_equition_solver(1, 70, 600)
        except TypeError:
            self.fail('Function must take 3 args')

    def test_raises_on_invalid_argument_type(self):
        from solver import squere_equition_solver
        with self.assertRaises(TypeError):
            squere_equition_solver(1, [-70], None)
