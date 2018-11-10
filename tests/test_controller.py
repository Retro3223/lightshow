from run import MyController

def test_controller(spidev):
    controller = MyController()

    controller.shutdown()
