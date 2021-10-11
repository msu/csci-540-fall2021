include Java
import 'org.apache.hadoop.hbase.client.HTable'
import 'org.apache.hadoop.hbase.client.Put'
import 'org.apache.hadoop.hbase.HBaseConfiguration'


def jbytes(*args)
  args.map {|arg| arg.to_s.to_java_bytes}
end

table = HTable.new(HBaseConfiguration.create, "wiki")

p = Put.new(*jbytes("Home"))

p.add(*jbytes("text", "", "This is page 1b!"))
p.add(*jbytes("revision", "author", "Dave M"))
p.add(*jbytes("revision", "commit", "Second edit from Dave"))

table.put(p)
