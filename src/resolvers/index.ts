import { Query } from './Query'
import { auth } from './Mutations/auth'

export const resolvers = { 
  Query, 
  Mutation: {
    ...auth,
  }
}