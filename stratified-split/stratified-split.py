import numpy as np

#strati
def stratified_split(X, y, test_size=0.2, rng=None):
    X = np.asarray(X)
    y = np.asarray(y)
    
    train_indices = []
    test_indices = []
    
    classes, counts = np.unique(y, return_counts=True)
    
    for cls, count in zip(classes, counts):
        cls_idx = np.where(y == cls)[0]
        

        if rng is not None:
            rng.shuffle(cls_idx)
        else:
            np.random.shuffle(cls_idx)
        

        n_test = int(round(count * test_size))
        
       
        if count > 1:
            n_test = min(n_test, count - 1)
        else:
            n_test = 0
        
        test_indices.extend(cls_idx[:n_test])
        train_indices.extend(cls_idx[n_test:])
    
    
    train_indices = np.sort(train_indices)
    test_indices = np.sort(test_indices)
    
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]