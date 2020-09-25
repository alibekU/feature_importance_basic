# a function that drops features one by one and measures the impact on the error
def dropcol_importances(initial_model, return_error, X, y):
    '''
        Returns a dataframe with differences in the error for each feature in 'X'
        by dropping each feature in 'X' by turn.
        The error is calculated by using function 'return_function' input parameter
        on 'y' input and predcitions 'initial_model' when given 'X'
    '''
    import sklearn.base
    model = sklearn.base.clone(initial_model)
    model.fit(X, y)
    baseline_error = return_error(model, X, y)
    imp = []
    for col in X_train.columns:
        X_train_new = X.drop(col, axis=1)
        model.fit(X_train_new, y)
        
        new_error = return_error(model, X_train_new, y)
        
        imp.append(new_error-baseline_error)
    
    imp = np.array(imp)
    I = pd.DataFrame(
            data={'Feature':X.columns,
                  'Importance':imp})
    I = I.set_index('Feature')
    I = I.sort_values('Importance', ascending=False)
    return I