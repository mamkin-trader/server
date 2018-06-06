import { GraphQLServer } from 'graphql-yoga'
import { Prisma } from './generated/prisma'
import { resolvers } from './resolvers'

const db = new Prisma({
  //typeDefs: './src/generated/prisma.graphql',
  endpoint: process.env.PRISMA_ENDPOINT,
  debug: true,
})

const server = new GraphQLServer({
  typeDefs: './src/schema.graphql',
  resolvers,
  context: req => ({ ...req, db }),
})

server.start(() => console.log(`Server is running on http://localhost:4000`))