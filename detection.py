from detecto import core, utils, visualize


def trainDataset():
    dataset = core.Dataset('C:\\Users\\sagef\\Documents\\Development\\python\\tensorLeague\\images\\Aatrox')
    model = core.Model(['Aatrox'])

    model.fit(dataset)


trainDataset()
