import * as jwt from 'jsonwebtoken'

export const auth = {
    async signup(parent, args, ctx, info) {
        // generate bcrypt password
        const user = await ctx.db.mutation.createUser({
            data: { ...args }
        })

        return { 
            token: jwt.sign({ userId: user.id }, process.env.APP_SECRET),
            user
        }
    },

    async login(parent, args, ctx, info) {
        const user = await ctx.db.query.user({ where: { email: args.email } })
        const valid = args.password === user.password

        if (!valid || !user) {
            // AUTH ERROR
            return
        }

        return {
            token: jwt.sign({ userId: user.id }, process.env.APP_SECRET),
            user
        }
    }
}