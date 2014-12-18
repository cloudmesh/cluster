name "hadoop"
description "set Hadoop attributes"
default_attributes(
  "hadoop" => {
    "distribution" => "bigtop",
    "core_site" => {
      "fs.defaultFS" => "hdfs://manager"
    },
    "yarn_site" => {
      "yarn.resourcemanager.hostname" => "manager"
    }
  }
)
run_list(
  "recipe[hadoop]"
)  
