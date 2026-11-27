INSERT INTO parking_lots(id,name,layout,layout_version)
SELECT '00000000-0000-4000-8000-000000000001','ParkOS Demo Lot',
'[{"type":"entrance","id":"IN"},{"type":"lane","id":"L1"},{"type":"slot","id":"A-01","zone":"Zone A","tier":"Standard","rate":3},{"type":"slot","id":"A-02","zone":"Zone A","tier":"Premium","rate":4},{"type":"exit","id":"OUT"}]'::jsonb,1
WHERE NOT EXISTS (SELECT 1 FROM parking_lots WHERE name='ParkOS Demo Lot');
