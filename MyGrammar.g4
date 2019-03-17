grammar MyGrammar;

select: SELECT STAR FROM WORD;

// SKIP

SPACE:                               [ \t\r\n]+    -> channel(HIDDEN);
SPEC_MYSQL_COMMENT:                  '/*!' .+? '*/' -> channel(HIDDEN);
COMMENT_INPUT:                       '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT:                        (
                                       ('-- ' | '#') ~[\r\n]* ('\r'? '\n' | EOF)
                                       | '--' ('\r'? '\n' | EOF)
                                     ) -> channel(HIDDEN);

SELECT              : 'SELECT';
STAR                : '*';
FROM                :'FROM';
fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;
WORD                : (LOWERCASE | UPPERCASE | '_')+ ;
