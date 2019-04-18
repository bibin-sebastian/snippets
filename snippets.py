
# Applying a function that takes muliple columns as args

df['d'] = df.apply(lambda x: some_func(a = x['a'], b = x['b'], c = x['c']), axis=1)
