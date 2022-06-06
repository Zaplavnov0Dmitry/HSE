plt.figure(figsize=(20,20))
plot_tree(model, feature_names=df.columns, fontsize = 3)
plt.savefig('tree.png', dpi=600)