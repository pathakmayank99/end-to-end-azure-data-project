USE advw_db
GO
CREATE OR ALTER PROC create_view @ViewName nvarchar(100) AS
BEGIN
    DECLARE @statement VARCHAR (MAX)
    SET @statement = N'CREATE OR ALTER VIEW ' + @ViewName + ' AS
        SELECT * FROM 
        OPENROWSET (
            BULK ''https://advwsa.dfs.core.windows.net/gold/SalesLT/' + @ViewName + '/'',
            FORMAT = ''DELTA''
        ) AS [result]'
EXEC (@statement)
END
GO