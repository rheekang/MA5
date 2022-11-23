for cat in ["train", "val", "test"]:
    _x, _y = locals()["x_" + cat], locals()["y_" + cat]
    print(cat, "x: ", _x.shape, "y:", _y.shape)
    np.savez_compressed(
        os.path.join("week73/", "%s.npz" % cat),
        x=_x,
        y=_y,
        x_offsets=x_offsets.reshape(list(x_offsets.shape) + [1]),
        y_offsets=y_offsets.reshape(list(y_offsets.shape) + [1]),
    )
