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