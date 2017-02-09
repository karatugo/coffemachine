from .EmailNotifier import EmailNotifier


class BeverageQuantityChecker:

    def isEmpty(water, milk):
        if(water == 0 or milk == 0):
            EmailNotifier.notifyMissingDrink()
            return True
