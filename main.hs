-- Aqui eu crio o data. Ou é E -> a ou E -> (E OP E)
data Expr = Var | Node Expr Char Expr

-- pra ficar show tlgd kkkk
instance Show Expr where
  show Var = "a"
  show (Node a b c) = "(" ++ show a ++ show b ++ show c ++ ")"

-- Chamo pra verificar se o operador é correto
-- Se for certo joga uma tupla, senao Nothing
parseOp :: String -> Maybe (Char, String)
parseOp [] = Nothing
parseOp (x : xs)
  | x `elem` "+-*/" = Just (x, xs)
  | otherwise = Nothing

-- Aqui começa a zoeira
parseExp :: String -> Maybe (Expr, String)
parseExp [] = Nothing -- Se for nada, retorna nada
parseExp (x : xs)
  | x == 'a' = Just (Var, xs) -- Caso base
  | x == '(' = case parseExp xs of -- Vai empilhando a fn sempre q aparecer um (
      Nothing -> Nothing
      Just (e1, resto1) ->
        -- o e1 é 'a' e o resto1 é o resto da str
        case parseOp resto1 of -- verifica o op
          Nothing -> Nothing
          Just (op, resto2) ->
            -- e2 é um op
            case parseExp resto2 of -- segundo 'a'
              Nothing -> Nothing
              Just (e2, resto3) ->
                case resto3 of -- se terminar com ) deu certo
                  (')' : resto4) -> Just (Node e1 op e2, resto4) -- aq pode ser um sub Expr de uma Expr maior, como se fosse uma arvore tlgd, ele vai montando
                  _ -> Nothing
  | otherwise = Nothing
