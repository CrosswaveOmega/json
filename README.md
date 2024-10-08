# json

A set of JSON files for developing applications with Helldivers 2.  
Intended to be updated a bit faster than the parent repo.

Presently, the only concern is updating the planet and assignment related JSON files.  Warbonds and items are untouched.


### Goals
Provide a set of 'static' information like planets, factions and sectors.
Applications that need this information (because they map from the API etc.)
can pull this data into their application and whenever new data is discovered and added
they can simply update this repository and get the updated information.

### Changes from parent repo
* The key of each planet's biome is based on the region names from https://github.com/shalzuth/HelldiversData
* Supercolony and Black Hole are considered biome types.
* Enviornmentals have an additional "Normal Temperature" type.

### How to use
While you can simply download the JSON files and use them directly
the recommended way is to use submodules.

The reasoning is that it's easy to update the JSON files with 1 command
and not have to manually check for updates.

To add this in your own project use the following command:
```shell
git submodule add https://github.com/CrosswaveOmega/json.git <folder>

# Or if you prefer using SSH
git submodule add git@github.com:CrosswaveOmega/json.git <folder>
```

To update the submodule simply run (see [docs](https://git-scm.com/book/en/v2/Git-Tools-Submodules#_pulling_in_upstream_changes_from_the_submodule_remote)):
```shell
# Folder is the directory in which your submodule lives
cd <folder>
git fetch
git merge origin/master
```

One (_small_) caveat is that when cloning your repository you have to tell Git to pull
the submodules as well. Fortunately, this is easy!
```shell
git clone --recurse-submodules <your git repo>

# Or if you already cloned the repo and forgot to init the submodules:
git submodule update --init <folder>
```

### Learn more
You can learn more about submodules on [Git's documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
