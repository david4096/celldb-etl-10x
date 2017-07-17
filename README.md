# celldb-etl-10x

This python module performs the task of adding 10xgenomics data to the celldb
functional genomics server.

This is done by providing the location of an HDF5 found that has either been
mounted to the Dockerfile, or available on the filesystem.

## Usage via python

To load your data into celldb using python, install the module and then direct
it at a celldb host, and a 10xgenomics h5 file.

```

pip install celldb-etl-10x
celldb_etl_10x localhost my_10x_data.h5

```

10xgenomics data are organized by `barcode`, which are considered the sample's
unique identifier in celldb. If you expect to load a very large amount of
samples consider adding a "salt" to the identifiers. This will append a small
string to each identifier to help guarantee uniqueness across datasets. The
salt is provided by the hash of the upsert statement used to create the row,
to help reduce duplication.

```

pip install celldb-etl-10x
celldb_etl_10x localhost my_10x_data.h5 --salt

```

## Usage via docker

If you would like to load a 10xgenomics data file using a docker instance,
first try:

```

docker run -it david4096/celldb-etl-10x celldb_etl_10x localhost my_10x_data.h5

```

This will run a docker container and print logs to the terminal. If no arguments
are provided 20k cells from the 10xgenomics Megacell demonstration will be
downloaded.

For 10xgenomics h5:

1) Copy HDF5 local
2) run_h5_to_tsv to generate both the features.tsv and to spawn processes that
will make out*.tsv to be added to the database.
3) Create feature table will generate a create table statement from the
features.tsv. Run this
4) create_table on 0.tsv which is a one line TSV that simply has the columns.
Run this statement
5) Create copy from statements for each of the out*.tsv files and run them.
