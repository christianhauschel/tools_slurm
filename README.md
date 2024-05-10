# tools_slurm

Output of `example.py`:

```bash
           Job: 91295   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Property         ┃ Value     ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ Name             │ obj       │
│ Status           │ COMPLETED │
│ User             │ user      │
│ Elapsed Time     │ 00:00:52  │
│ CPU Time         │ 00:16:28  │
│ Allocated Memory │ 50G       │
│ Allocated CPUs   │ 19        │
│ Allocated Nodes  │ 1         │
│ Partition        │ bravo     │
│ Nodes            │ [44]      │
└──────────────────┴───────────┘

               Cluster                
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property   ┃ Value                 ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Partitions │ alpha, bravo, charlie │
└────────────┴───────────────────────┘

                  Partition: bravo                   
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Property       ┃ Value                            ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Nodes          │ [41, 42, 43, 44, 45, 46, 47, 48] │
│ Allocated CPUs │ 80                               │
│ Idle CPUs      │ 80                               │
│ Other CPUs     │ 0                                │
└────────────────┴──────────────────────────────────┘

       Node: node41       
┏━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Property       ┃ Value ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Allocated CPUs │ 20    │
│ Idle CPUs      │ 0     │
│ Other CPUs     │ 0     │
└────────────────┴───────┘
```