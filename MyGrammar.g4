grammar MyGrammar;
sentence: words EOF ;  //root: select_sentence, update_sentence etc
words: SELECT STAR FROM WORD ;

// SKIP
WS : [ \t\r\n]+ -> skip ;

SELECT  : 'SELECT';
STAR  : '*' ;
FROM  : 'FROM' ;
LOWERCASE  : [a-z] ;
UPPERCASE  : [A-Z] ;
WORD : (LOWERCASE | UPPERCASE)+ ;
END : ';' ;
STRING : '"'[^"]*'"' ;
