grammar MyGrammar;

sentence: words* EOF ;
words: SELECT STAR FROM WORD ;
// SKIP
WS : [ \t\r\n]+ -> skip ;

SELECT  : 'SELECT';
STAR  : '*' ;
FROM  : 'FROM' ;
LOWERCASE  : [a-z] ;
UPPERCASE  : [A-Z] ;
WORD : (LOWERCASE | UPPERCASE)+ ;
