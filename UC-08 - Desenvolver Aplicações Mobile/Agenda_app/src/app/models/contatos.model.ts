import { Guid } from "guid-typescript";

export interface Contatos {
    id: Guid
    nome: string
    sobrenome: string
    tipo_num: string
    num: string
    email: string
}