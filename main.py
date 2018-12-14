from code.algorithms.smartgridBattery import SmartGridBattery
from code.algorithms.smartgridHillclimber import SmartGridHillclimber
from code.algorithms.smartgridShuffle import SmartGridShuffle
from code.algorithms.smartgridRelocation import SmartGridRelocation
from code.algorithms.smartgridSteepest import SmartGridSteepest
from code.algorithms.smartgridStochastic import SmartGridStochastic
from datetime import datetime


def main():
    start_time = datetime.now()

    for i in range(10):
        SmartGridHillclimber()
        if i == 8:
            end_time = datetime.now()
            print('Duration: {}'.format(end_time - start_time))


if __name__ == "__main__":
    main()
